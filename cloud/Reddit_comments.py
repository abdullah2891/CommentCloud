import praw

__author__ = 'Abdullah_Rahman'


class Reddit_comments:
    def __init__(self):
        self.r=praw.Reddit('test')

    def return_comments(self,URL):
        submission=self.r.get_submission(url=URL)
        comments=submission.comments
        flat_comments=praw.helpers.flatten_tree(comments)

        s=""

        for comment in flat_comments:
            try:
                s+=comment.body
            except AttributeError:
                pass

        return s



def main():
    url=raw_input("Enter URL :")
    r=Reddit_comments()
    comments=r.return_comments(url)
    print comments


