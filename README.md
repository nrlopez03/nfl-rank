# nfl-rank
Nicholas Lopez and Elliot Chin

December 12, 2021

## About
Massey Matrices use point differential to measure the strength of teams. However, point differential isn’t a perfect measure; often times teams up or down by a significant amount pull starters, inflating or deflating point differentials. Instead of simply using point differentials, we could combine point differentials with other differential variables, such as turnovers or rushing yards. First, each differential must be normalized to have a consistent mean and standard deviation. Then, differentials can be added together with custom weights- for example, Massey Matrices could be half dependent on point differential, and half dependent on interception differential. We have created a web application that allows users to use this strategy create custom NFL rankings. The application uses data9 across multiple fields, from record to penalty differential. The web application can be found at http://nflrank.herokuapp.com/, and the source code can be found at https://github.com/nrlopez03/nflrank. This application was made entirely from scratch. As far as we are aware, this has never been made before in such a fashion. The calculations are made real-time, followingMassey’s Method exactly. No packages for matrix multiplication, data interpolation, or other shortcuts were used. All math is done entirely using matrices represented as nested lists in Python, and the data is displayed through HTML and JavaScript. The program allows users to set weightings for such a factor. As a default, the record is set to 100% of the weighting and must always have some non-zero weighting. Users may alter the weightings, which are applied to unique, individual y columns that contain data from every single game played through Week 12 of the NFL season. These y columns are added together to contain the resultant final y column. The rest of the calculations use Massey’s Method and the method of least squares to determine the ranking values for the unique parameters.
