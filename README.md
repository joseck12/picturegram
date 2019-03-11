INSTAGRAM.

A clone of the website for the popular photo app Instagram.
By Joseck Ogachi

Description
This application allows users to sign up then they can create a profile and upload images for other users to like and comment,and users can also follow each other to ensure that they get timely notifications.
Setup/Installation Requirements
installations required
Install python version  3.6
Install django==1.11.5
Install Pipenv pip install --user pipenv
Install virtual environment and activate it

In order to clone , follow the procedure below;
On GitHub, navigate to the main page of the repository.
Under the repository name, click Clone or download.
Copy the link.
Open Terminal.
Change the current working directory to your preffered location.
Type git clone, and then paste the URL you copied in the above step.
git clone https://github.com/joseck12/picturegram.git Press Enter.

#creating a database

psql
CREATE DATABASE picturegram;
connect to the database \c picturegram;
check if tables have been created \dt
install dependancies -pip3 install -r requirements.txt

#Run migrations

python3.6 manage.py migrate
python3.6 manage.py makemigrations pictureapp

#Running the app

python3.6 manage.py runserver

#testing

python3.6 manage.py test picturegram
#SPECIFICATIONS | Behaviour | Input | Output |

| Display Images| On the HomePage| User can view different Images| | Image expand | * On the Landing Page*| User can click on an image to view more details| | As an Admin Sign in| * On The Admin Dashboard*| Post images| | As A User | *On Profile Page| Edit Profile Page|

Technologies Used
HTML
CSS
Python
Django
Postgres
javascript

Support and contact details
jogachi4@gmail.com
0726825457

Known Bugs
There are no know bugs,incase of any reach me on the above contact details.

License
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE Copyright (c) {2018} {By Joseck Ogachi}

##live link to Heruko 
