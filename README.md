# RestStoneAPI
## Index
<ul>
    <li><a href="#about">About the Project</a></li>
    <li><a href="#UML">UML Diagram</a></li>
    <li><a href="#Run">How to Run</a></li>
    <ul>
        <li><a href="#Online">Online 🌏</a></li>
        <li><a href="#Docker">Docker Image 🐳</a></li>
        <li><a href="#Cloning">Cloning Repo ⬇️</a></li>
    </ul>
    <li><a href="#Running">Running</a></li>
    <li><a href="#Tests">Tests</a></li>
    <ul>
        <li><a href="#How_Tests">How to Run the Tests</a></li>
    </ul>
      <li><a href="#Notes">Author's Notes</a></li>

</ul>

<h2 id ="about">About </h2>
 Inspired by my favorite game Dark Souls, there is an item called Soapstone that leaves messages for other players. So I decided to create RestStone
 (since it's a REST API) to leave messages for other people. Working as a CRUD, it is possible to create messages, delete, update and read. My main 
 intention was to create an API service to supply a bash script that would make it so that whenever the programmer opened the terminal, a message 
 previously written by another programmer was shown, he could vote for the best messages and could choose the minimum number of votes in the message 
 needs to have in order to appear for him. This project arose from a challenge for an internship in software engineering at Hashdex
 
 <h2 id ="UML">UML Diagram </h2>
 
![Diagrama em branco(1)](https://user-images.githubusercontent.com/72756630/209347206-d874244f-f374-4bd8-a6b4-6a93e4db49f7.png)

 <h1 id ="Run">How to Run 🚀</h1>
 
 <h2 id ="Online">Online 🌏</h2>
<h4>☁️  Hosted on AWS ☁️  </h4>

> **_NOTE:_** Paste this link into your browser

  ```ec2-54-164-155-178.compute-1.amazonaws.com/apidoc/swagger```

<h5></h5>
<h5> Set up an EC2 instance on AWS to host my API. Using nginx, bash and systemd scripts. <br>  I intend to keep the server running for a week, during the project evaluation period by Hashdex, closing the server on 12/30/2022 at 12:00</h5>
<hr>
<br> 
 
 <h2 id ="Docker">Docker Image 🐳</h2>
 <h4>📋 Prerequisites </h4>
   <ul>
      <li>You will need to have previously installed docker, you can install it by <a href="https://docs.docker.com/get-docker/">clicking here </a></li>
   </ul>
 <h4>🔧 Setup </h4>
    <ol>
      <h3>1️⃣ Download image from DockerHub<h3>
      
 
     docker push atlasgold31/api-crud-flask

 <h3> 2️⃣ Start the container</h3>
     
     docker run -p 1234:1234 atlasgold31/api-crud-flask


 <h3> 3️⃣ Then Run</h3>
        <h4> <a href="#Running">Click Here</a></h4> 
   </ol>
<br>
<hr>
 
<h2 id ="Cloning">Cloning Repo⬇️</h2>
<h4>📋 Prerequisites </h4>
   <ul>
      <li><h5> You will need to have previously installed GIT, you can install it by <a href="https://git-scm.com/book/en/v2/Getting-Started-Installing-Git/">clicking here </a> <h5></li>
      <li><h5> You will need python version 3.10 or greater, you can install it by <a href="https://www.python.org/downloads/">clicking here </h5> </li>
   </ul>
   
 <h4>🔧 Setup </h4>
<ol>
      <h3>1️⃣ Clone the repository</h3>

**HTTPS**

```
git clone https://github.com/AtlasGold/RestStoneAPI.git
```

**SSH**

```
git clone gitgit@github.com:AtlasGold/RestStoneAPI.git
```

<h3> 2️⃣ Enter the folder</h3>

```
cd RestStoneAPI
```

<h3> 3️⃣  Install Dependencies </h3>

> **_NOTE:_** If you are on windows run the terminal as administrator


```
sudo pip install -r requirements.txt
```

<h3> 4️⃣ Start the API </h3>

> **_NOTE:_** If you are on windows run python app.py


```
python3 app.py
```


<h3> 5️⃣ Run the API </h3>
  <h4> <a href="#Running">Click Here</a></h4> 

</ol>

<hr>
<br>

<h1 id="Running"> Running </h1
<h4>📋 Prerequisites </h4>
<h5> You must have already started the API server, following the steps of running a <a href="#Docker">Docker Image 🐳</a>  or <a href="#Cloning">Cloning Repo ⬇️</a></h5>

<h4>🔧 Setup </h4>
<h5>With the server running, you should see a similar message in your terminal </h5>

![image](https://user-images.githubusercontent.com/72756630/209360221-2d75010d-0300-47af-a130-522888aefdc2.png)

<h5> you will need to open your browser and add this URL. (<a href="http://localhost:1234/apidoc/swagger"> or click here </a>)</h5>

```
http://localhost:1234/apidoc/swagger
```
<h4>You will be on this screen </h4>

![image](https://user-images.githubusercontent.com/72756630/209361666-6c474b2b-3a62-49e8-9fba-715a013f2d9f.png)


<h4>You can now manually test endpoints and message CRUD</h4>

<h1 id="Tests"> Tests </h1
<h4>📋 Prerequisites </h4>

<h5> You must have already started the API server, following the steps of <a href="#Cloning">Cloning Repo ⬇️</a></h5>

> **_NOTE:_** If you are running on Docker clone the repo and install dependencies (steps 1 to 3).

          
<h4 id="How_Tests">🔧 Testing </h4>

```
python3 -m pytest test
```
          
> **_NOTE:_** This command must be run in the root of the project.

          
          

<h1 id="Notes"> Author's Notes </h1>

<h3> Talking about what I think about the project and what I felt while developing it </h3>

This project came as a challenge for an internship vacancy and like all my projects I want to do the best I can,
I admit that I'm not very good, but I realized that I could improve my developer skills A LOT, in this project I 
understood the importance of unit tests, when I started writing them I realized how bad my code was, and I needed
to refactor a lot of things. I learned a lot about the architecture of an API in python, I only had experience
with API development in javascript but because Hashdex uses a lot of python I decided to use python as a way to get closer

<h3> Talking about Frameworks and choices </h3>
I chose to use Flask because, unlike Django, it gives me a blank canvas and I have the freedom to do it the way I imagined it.
The database I used was TinyDB, it is not recommended for large projects, but I decided to take a chance on a new database to 
learn, database is my passion, and I am very happy when I try to learn a DBMS/ORM new, and I can extract at least what I needed for my project

<h3> Talking about unit testing </h3>
I always knew the importance of unit tests, but in this project I fully understood how important they are 
in any project, I wanted to test as much as I could have my API and I feel that it was still not enough, 
I am delivering the project with 40 tests unit tests, and I feel that they were not enough, I wish I had
more time to dedicate myself to creating my unit tests

<h3> Talking about acquired knowledge </h3>
During the interview, the interviewer said that they use a lot of cloud like AWS in Hashdex, so I decided that my 
API also uses such a tool, I put all my DevOps study into practice and managed to configure the connection of a
virtual machine to the internet. I learned a lot about HTPP codes, much more than in college, I understood in which
situation we use each of the codes and I tried to use the best practices in my API.
Speaking of good practices, I tried to read python articles about Best Practices when building a project in python, 
from how to separate folders to how to write variable names and comments

<h3> Final Considerations </h3>
I feel that I learned a lot from this project, regardless of whether I get the job or not, I already know that 
it was worth it. I had fun every moment while creating this API and I could be sure that I am doing what I love.
Thanks for the opportunity.
