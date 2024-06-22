# JoSAA DATA ANALYSIS PORTAL 


<section>
        <p>This project aims to create a portal to explore the seat allotment statistics of the Joint Seat 
Allocation Authority (JoSAA) until 2023. The portal allows users to analyse the data and provides 
insights and visualisations based on the JoSAA seat allotment data from 2016 to 2023. Below are 
the key objectives and technologies used in this project.</p>
    </section>
<!--     <section>
        <h2>Project Overview</h2>
        <p>The primary aim of this project is to facilitate a detailed exploration and analysis of JOSAA seat allotment data spanning from 2016 to 2023. By leveraging advanced data cleaning, analysis, and visualisation techniques, the portal offers users an intuitive interface to examine various aspects of seat allotment trends over the years.</p>
    </section> -->
   <section>
         <h2>Goals</h2>
         <ol>
            <li> Perform data cleaning and exploratory data analysis (EDA) on the JoSAA seat allotment data.</li>
            <li> Create a SQLite database from the cleaned data and perform queries on it.</li>
            <li> Develop a website to present the analysis using various charts and tables.</li>
         </ol>
</section>
   
<section>
        <h2>Tech Stack / Frameworks</h2>
        <ul>
            <li><strong>Frontend</strong>: HTML, CSS, JavaScript</li>
            <li><strong>Backend</strong>: Django, SQLite</li>
            <li><strong>Data Scraping</strong>: Selenium</li>
            <li><strong>Data Cleaning</strong>: NumPy, Pandas </li>
            <li><strong>Visualisation</strong>: Chart.js </li>
           </ul>
</section>
   

  <section>
         <h2>Usage</h2>
         <li><strong>To run the JoSAA Data Analysis Portal directly, click <a href="https://dsamanta64.pythonanywhere.com/">here</a>.</strong></li>
         <strong>Note</strong>:
         <ol>
         <li> It is advised to open the website on PC/Laptop. Still, if you are using it on mobile, please turn on the desktop mode for desired visualization.</li>
         <li>
          Due to the website we hosted our program on, there is a 1-2 second lag in 
the dropdown menus of each section. Please be patient as we work to fix this 
issue.</li></ol><br>

 <li><strong>To run the JoSAA Data Analysis Portal locally, follow these steps:</strong></li>
    
<ol>
            <li> Clone the repository:<br><br> 
git clone https://github.com/debabrata64/JOSAA_DATA_ANALYSIS_PORTAL.git</li><br>
            <li> Change to the project directory:<br><br>
cd JOSAA_DATA_ANALYSIS_PORTAL</li><br>
            <li> Install the required Python packages:<br><br>
pip install -r requirements.txt</li><br>
             <li> Run database migrations:<br><br>
python manage.py migrate</li><br>
            <li> Start the development server:<br><br>
python manage.py runserver</li><br>
            <li> Access the portal in your web browser at <a href="http://localhost:8000/">http://localhost:8000/</a>.</li><br>
        </ol><br>

<li><strong>See the demonstration of JoSAA Data Analysis Portal <a href="https://drive.google.com/file/d/1zQ11zSQZDUd7b2v3kjtSGrUtSKXuNXpq/view?usp=drive_link">here</a>.</strong></li><br>


   </section> 
   
<!-- <section>
         <h2>Data Extraction and Cleaning</h2>
        The JoSAA seat allotment data has been provided and is ready for analysis. The data cleaning 
process involves using the NumPy and Pandas libraries to clean and transform the data as 
required for analysis. -->
           
            
</ul>
</section>
   
<section>
        <h2>Data Insights and Analysis</h2>
        <p>The portal offers several sections for in-depth data analysis:</p>
        <ol>
            <li><strong>Round-wise Trends:</strong> Check the opening and closing ranks for all six rounds for a particular year.</li>
            <li><strong>Year-wise Trends:</strong> Examine the opening and closing ranks from 2016-2023 for a specific round.</li>
            <li><strong>Top 20 Courses:</strong> Discover the top 20 courses suitable for you based on your achieved rank.</li>
            <li><strong>Course Comparison:</strong> Compare two courses from the same or different colleges and assess their popularity.</li>
            <li><strong>Best College:</strong> Identify the best colleges based on their popularity for a particular course.</li>
            <li><strong>Category-wise Analysis:</strong> Analyse the category-wise differences between opening and closing ranks.</li>
        </ol>
</section>
   
   
   <section>
   <h2>Contributions</h2>
        Contributions to this project are welcome! If you have any suggestions, improvements, or new 
features to add, please open an issue or submit a pull request.
    </section>
   
   
   <section>
   <h2>Acknowledgements</h2>
        <p>This project utilises several open-source libraries and frameworks:</p>
          <ul>
            <li><strong>Django</strong> </li>
            <li><strong>Selenium</strong>  </li>
            <li><strong>Pandas</strong></li>
            <li><strong>NumPy</strong> </li>
            <li><strong> Chart.js</strong></li>
           </ul>
        <p>We extend our heartfelt thanks to the developers of these tools for their invaluable contributions 
to the open-source community.<br>
This project was made possible thanks to the support and allocation of this summer project by 
the Coding Club, IIT Guwahati.</p>
    </section>
  
<section>
         <h3>Contributors:</h3>
         <ul>
            <li> Debabrata Samanta, MSc Mathematics</li>
            <li> Pratham Doiphode, MSc Mathematics and Computing</li>
            <li> Priyanshu Kumar, MSc Mathematics</li>
            <li> Sourish Maity, MSc Mathematics and Computing</li> 
        </ul>
    </section>
    

<section>
  
 Thank you for visiting the JoSAA Data Analysis Portal. We hope you find this resource insightful 
and useful in your academic and research endeavours.
    </section>