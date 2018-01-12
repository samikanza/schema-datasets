import urllib.request
import json
from github import Github
import xlsxwriter

# Login to github 
# replace these with your own login details! 
g = Github(@GitHubName, @GitHubPassword)

# access the repo
repo_name = 'schemaorg/schemaorg'
repo = g.get_repo(repo_name)
issues = repo.get_issues()

#cellvariablse
issue_id = 'A'
issue_user_id = 'B'
issue_title = 'C'
issue_body = 'D'
issue_comments = 'E'
issue_commenters = 'F'
number_of_comments = 'G'

x = 1

workbook = xlsxwriter.Workbook('schema-org-github.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write('A1', 'issue_id')
worksheet.write('B1', 'issue_user_id')
worksheet.write('C1', 'issue_title')
worksheet.write('D1', 'issue_body')
worksheet.write('E1', 'issue_comments')
worksheet.write('F1', 'issue_commenters')
worksheet.write('G1', 'number_of_comments')

for issue in issues:
	x = x+1
	comment_string = ""
	commenters_string = ""
	for comment in issue.get_comments():
		comment_string += "#### new comment by " 
		comment_string += str(comment.user.id) 
		comment_string += " ####\n"
		comment_string += comment.body 
		comment_string += "\n"
		commenters_string += "comment: "
		commenters_string += str(comment.user.id) 
		commenters_string += "\n"
	
	issue_id_x = str(issue_id) + str(x)
	issue_user_id_x = str(issue_user_id) + str(x)
	issue_title_x = str(issue_title) + str(x)
	issue_body_x = str(issue_body) + str(x)
	issue_comments_x = str(issue_comments) + str(x)
	issue_commenters_x = str(issue_commenters) + str(x)
	number_of_comments_x = str(number_of_comments) + str(x)

	worksheet.write(issue_id_x, str(issue.id))
	worksheet.write(issue_user_id_x, str(issue.user.id))
	worksheet.write(issue_title_x, str(issue.title))
	worksheet.write(issue_body_x, str(issue.body))
	worksheet.write(issue_comments_x, str(comment_string))
	worksheet.write(issue_commenters_x, str(commenters_string))
	worksheet.write(number_of_comments_x, str(issue.comments))

workbook.close()
	
print ('file written successfully')
