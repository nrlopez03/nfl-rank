# nfl-rank
Nicholas Lopez and Elliot Chin

December 12, 2021

## About
Clearly, there are boundless limits for the use of Massey Matrices. To emphasize this perspective and show Massey Matrices in a new light, we created a web application to allow users to create custom NFL rankings. The application uses data across multiple fields, from record to penalty differential. The web application can be found [here](http://nfl-rank.herokuapp.com/), and the source code can be found at [here](https://github.com/nrlopez03/nfl-rank). It is important to note that was done entirely from scratch. As far as we are aware, this has never been made before in such a fashion. The calculations are made real-time, following Massey's Method exactly. No packages for matrix multiplication, data interpolation, or other shortcuts were used. All math is done entirely using matrices represented as nested lists in Python, and the data is displayed through HTML and JavaScript. 

The program allows users to set weightings for such a factor. As a default, the record is set to 100% of the weighting and must always have some non-zero weighting. Users may alter the weightings, which are applied to unique, individual y columns that contain data from every single game played through Week 12 of the NFL season. These y columns are added together to contain the resultant final y column. The rest of the calculations use Massey's Method and the method of least squares to determine the ranking values for the unique parameters. 
