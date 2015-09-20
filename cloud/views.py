import matplotlib
matplotlib.use('agg')

from django.shortcuts import render,HttpResponse
from .models import UploadCloud
from Reddit_comments import Reddit_comments
from wordcloud import WordCloud
from matplotlib import pylab
from pylab import *
import PIL, PIL.Image, StringIO
import praw

# Create your views here.




def view(request):
     return render(request, 'cloud/form.html',{})

def test(request):
     #url='https://www.reddit.com/r/funny/comments/3lcf7d/what_i_imagine_entering_the_job_market_in_the_90s/'
     if request.method=='POST':
        url=request.POST.get('user')
        r=Reddit_comments()
        comments=r.return_comments(url)
        wordcloud = WordCloud(max_font_size=40).generate(comments)
        figure()
        imshow(wordcloud)

        buffer = StringIO.StringIO()
        canvas = pylab.get_current_fig_manager().canvas
        canvas.draw()
        pilImage = PIL.Image.fromstring("RGB", canvas.get_width_height(), canvas.tostring_rgb())
        pilImage.save(buffer, "PNG")
        return HttpResponse(buffer.getvalue(), content_type="image/png")


def server_error(request):
        return render(request, 'cloud/index.html',{})




