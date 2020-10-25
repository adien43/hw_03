import praw
import random
import datetime
import time


# FIXME:
# This part generates the individals comments x 100000

def generate_comment_0():
    #text = "Trump's hair and tan reminds me a handsome older version of Ken."
    names = ['Trump', 'Presdient','Donald']
    name = random.choice(names)
    text = name + "'s hair and tan reminds me a handsome older version of Ken"

    return text

def generate_comment_1():
    #text = 'Tiger Woods learned golf from President Trump'
    learns = ['mastered','got the hang of','was coached by']
    learn = random.choice(learns)
    text = "Tiger Woods " + learn + " golf from Presdient Trump"
    return text

def generate_comment_2():
    #text = 'Trump had the best parties in his hotels'
    events = ['gatherings','hang outs','parties']
    event = random.choice(events)
    text = 'Trump had the best ' + event + ' in his hotels'
    return text

def generate_comment_3():
    #text = 'Biden has too much white hair to be president'
    names = ['Biden','The deomcacratic nominee','Hunter']
    name = random.choice(names)
    text = name + ' has too much white hair to be president'
    return text

def generate_comment_4():
    #text = 'Biden cannot talk because President stays quiet'
    actions = ['speak','argue','talk']
    action = random.choice(actions)
    text = "Biden cannot " + action + ' because Trump stays quiet'
    return text

def generate_comment_5():
    #text = "The color blue is boring thus, I do(nt like Biden's tie"
    clothings = ['eyes','tie']
    clothing = random.choice(clothings)
    text = "The color blue is boring thus, I dont like Biden's " + clothing 
    return text


def generate_comment():
    comments = [generate_comment_0(), generate_comment_1(), generate_comment_2(), generate_comment_3(), generate_comment_4(),generate_comment_5()]
    comment = random.choice(comments)
    return comment
    '''
    #This function should randomly select one of the 6 functions above,
    #call that function, and return its result.
    '''

#for i in range (10000):
    #print(generate_comment())
# connect to reddit 
reddit = praw.Reddit('bot1')

# connect to the debate thread
reddit_debate_url = 'https://www.reddit.com/r/csci040temp/comments/jhb20w/2020_debate_thread/'
submission = reddit.submission(url=reddit_debate_url)
#print(submission)
# each iteration of this loop will post a single comment;
# since this loop runs forever, your bot will continue posting comments forever;
# (this is what makes it a deamon);
# recall that you can press CTRL-C in the terminal to stop your bot
#
# HINT:
# while you are writing and debugging your code, 
# you probably don't want it to run in an infinite loop;
# you can change this while loop to an if statement to make the code run only once


while True:

    # printing the current time will help make the output messages more informative
    # since things on reddit vary with time
    print()
    print('new iteration at:',datetime.datetime.now())
    print('submission.title=',submission.title)
    print('submission.url=',submission.url)

    # FIXME (task 0): get a list of all of the comments in the submission
    # HINT: this requires using the .list() and the .replace_more() functions
    all_comments = []
    submission.comments.replace_more(limit=None)
    for comment in submission.comments.list():
        all_comments.append(comment)
    #print(all_comments)
    
    # HINT: 
    # we need to make sure that our code is working correctly,
    # and you should not move on from one task to the next until you are 100% sure that 
    # the previous task is working;
    # in general, the way to check if a task is working is to print out information 
    # about the results of that task, 
    # and manually inspect that information to ensure it is correct; 
    # in this specific case, you should check the length of the all_comments variable,
    # and manually ensure that the printed length is the same as the length displayed on reddit;
    # if it's not, then there are some comments that you are not correctly identifying,
    # and you need to figure out which comments those are and how to include them.
    print('len(all_comments)=',len(all_comments))

    # FIXME (task 1): filter all_comments to remove comments that were generated by your bot
    # HINT: 
    # use a for loop to loop over each comment in all_comments,
    # and an if statement to check whether the comment is authored by you or not
    not_my_comments = []
    for comment in all_comments:
        if comment.author.name == "bottomsup40":
            pass
        else:
            not_my_comments.append(comment)
    #print(not_my_comments)
    

    # HINT:
    # checking if this code is working is a bit more complicated than in the previous tasks;
    # reddit does not directly provide the number of comments in a submission
    # that were not gerenated by your bot,
    # but you can still check this number manually by subtracting the number
    # of comments you know you've posted from the number above;
    # you can use comments that you post manually while logged into your bot to know 
    # how many comments there should be. 
    print('len(not_my_comments)=',len(not_my_comments))

    # if the length of your all_comments and not_my_comments lists are the same,
    # then that means you have not posted any comments in the current submission;
    # (you bot may have posted comments in other submissions);
    # your bot will behave differently depending on whether it's posted a comment or not
    has_not_commented = len(not_my_comments) == len(all_comments)
    
    if has_not_commented:
        try:
            new_comment = generate_comment()
            submission.reply(new_comment)
            print("new comment")
        except:
            print("exception found")
            time.sleep(5)
        # FIXME (task 2)
        # if you have not made any comment in the thread, then post a top level comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit
    
    else:
        # FIXME (task 3): filter the not_my_comments list to also remove comments that 
        # you've already replied to
        # HINT:
        # there are many ways to accomplish this, but my solution uses two nested for loops
        # the outer for loop loops over not_my_comments,
        # and the inner for loop loops over all the replies of the current comment from the outer loop,
        # and then an if statement checks whether the comment is authored by you or not
        comments_without_replies = []
        for comment in not_my_comments:
            isMyName = False
            for replies in comment.replies.list():
                if replies.author.name == 'bottomsup40':
                    isMyName = True 
                else:
                    pass
            if isMyName == False:
                comments_without_replies.append(comment)
            else:
                pass


        # HINT:
        # this is the most difficult of the tasks,
        # and so you will have to be careful to check that this code is in fact working correctly
        print('len(comments_without_replies)=',len(comments_without_replies))
    
        # FIXME (task 4): randomly select a comment from the comments_without_replies list,
        # and reply to that comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit

        try:
            comment_reply = random.choice(comments_without_replies)
            new_comment = generate_comment()
            comment_reply.reply(new_comment)
            print('new reply')
        except:
            print("exception found")
            time.sleep(5)


    
    # FIXME (task 5): select a new submission for the next iteration;
    # your newly selected submission should have a 50% chance of being the original submission
    # (url in the reddit_debate_url variable)
    # and a 50% chance of being randomly selected from the top submissions to the csci040 subreddit for the past month
    # HINT: 
    # use random.random() for the 50% chance,
    # if the result is less than 0.5,
    # then create a submission just like is done at the top of this page;
    # otherwise, create a subreddit instance for the csci40 subreddit,
    # use the .top() command with appropriate parameters to get the list of all submissions,
    # then use random.choice to select one of the submissions

r = random.random()
print(r)
if r < 0.5:
    print('create a submission just like is done at the top of this page')
    reddit_debate_url = 'https://www.reddit.com/r/csci040temp/comments/jhb20w/2020_debate_thread/'
    submission = reddit.submission(url=reddit_debate_url)
    print(submission.title)
else:
    print('create a subreddit instance for the csci40 subreddit use random.choice to select one of the submissions')
    submission_2 = reddit.subreddit("csci040temp").random()
    print(submission_2.title)
    submission = submission_2


