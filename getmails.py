__author__ = 'fissalalsharef'


import outlook
mail = outlook.Outlook()
mail.login('fissalalsharef@std.sehir.edu.tr','feasal12354568+')
mail.inbox()
print mail.unread()



