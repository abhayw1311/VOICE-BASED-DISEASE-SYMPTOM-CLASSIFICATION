-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 01, 2024 at 01:59 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `diseases_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `doctor`
--

CREATE TABLE `doctor` (
  `did` int(200) NOT NULL,
  `name` varchar(200) NOT NULL,
  `address` varchar(200) NOT NULL,
  `contact` varchar(200) NOT NULL,
  `specialist` varchar(200) NOT NULL,
  `type` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `doctor`
--

INSERT INTO `doctor` (`did`, `name`, `address`, `contact`, `specialist`, `type`) VALUES
(1, 'Saboo Diabetes And Thyroid Centre', 'Ravinagar road, Amravati - 444601, Opposite Samarth Highschool', '9423423422', 'Diabetologist', 'Private'),
(2, 'Saboo Diabetes And Thyroid Centre', 'Ravinagar road, Amravati - 444601, Opposite Samarth Highschool', '9423423422', 'Thyroid', 'Private'),
(3, 'Shri Mistry Sealth Centre', 'Bazzar Gate Street Fotr, Amravati, Amravati ?444601, Amravati', '72125630', 'Diabetologist', 'Private'),
(4, 'Shri Mistry Sealth Centre', 'Bazzar Gate Street Fotr, Amravati, Amravati ?444601, Amravati', '72125630', 'Dentists', 'Private'),
(5, 'Shri Mistry Sealth Centre', 'Bazzar Gate Street Fotr, Amravati, Amravati ?444601, Amravati', '72125630', 'Dermatologist', 'Private'),
(6, 'Shri Mistry Sealth Centre', 'Bazzar Gate Street Fotr, Amravati, Amravati ?444601, Amravati', '72125630', 'Psychiatrists', 'Private'),
(7, 'Shri Mistry Sealth Centre', 'Bazzar Gate Street Fotr, Amravati, Amravati ?444601, Amravati', '72125630', 'Psychologist', 'Private'),
(8, 'Shri Mistry Sealth Centre', 'Bazzar Gate Street Fotr, Amravati, Amravati ?444601, Amravati', '72125630', 'Oncologists', 'Private'),
(9, 'Shri Mistry Sealth Centre', 'Bazzar Gate Street Fotr, Amravati, Amravati ?444601, Amravati', '72125630', 'Radiologist', 'Private'),
(10, 'Amit Achliya', '1St Floor Faida Building, Amravati 444601, Near Savkar Bhavan Jaystambh squre', '9422265961', 'Cardiologist', 'Private'),
(11, 'Amit Achliya', '1St Floor Faida Building, Amravati 444601, Near Savkar Bhavan Jaystambh squre', '9422265961', 'Diabetologist', 'Private'),
(12, 'Amit Achliya', '1St Floor Faida Building, Amravati 444601, Near Savkar Bhavan Jaystambh squre', '9422265961', 'Thyroid', 'Private'),
(13, 'Amit Achliya', '1St Floor Faida Building, Amravati 444601, Near Savkar Bhavan Jaystambh squre', '9422265961', '2D Echo', 'Private'),
(14, 'Amit Achliya', '1St Floor Faida Building, Amravati 444601, Near Savkar Bhavan Jaystambh squre', '9422265961', 'Diabetic Centres', 'Private'),
(15, 'Amit Achliya', '1St Floor Faida Building, Amravati 444601, Near Savkar Bhavan Jaystambh squre', '9422265961', 'Cardiologist 2D Echo', 'Private'),
(16, 'Amit Achliya', '1St Floor Faida Building, Amravati 444601, Near Savkar Bhavan Jaystambh squre', '9422265961', 'Hypertension', 'Private'),
(17, 'Advait Mahalley', 'Amravati 444601, Bhau Colony Radha Nagar', '7212551143', 'Diabetologist', 'Private'),
(18, 'Advait Mahalley', 'Amravati 444601, Bhau Colony Radha Nagar', '7212551143', 'Cardiologist', 'Private'),
(19, 'Amaravati City Multispeciality Hospital', 'Kalyan Nagar Square, Rukhmini Nagar Road, Rukhmini Nagar, Amravati ?444606, Opp Dr Chaudhary Homeopathic Hospital', '9765492712', 'General Surgeon', 'Private'),
(20, 'Amaravati City Multispeciality Hospital', 'Kalyan Nagar Square, Rukhmini Nagar Road, Rukhmini Nagar, Amravati ?444606, Opp Dr Chaudhary Homeopathic Hospital', '9765492712', 'Homeopathic Doctors For Diabetes', 'Private'),
(21, 'Amaravati City Multispeciality Hospital', 'Kalyan Nagar Square, Rukhmini Nagar Road, Rukhmini Nagar, Amravati ?444606, Opp Dr Chaudhary Homeopathic Hospital', '9765492712', 'Diabetologist', 'Private'),
(22, 'Amaravati City Multispeciality Hospital', 'Kalyan Nagar Square, Rukhmini Nagar Road, Rukhmini Nagar, Amravati ?444606, Opp Dr Chaudhary Homeopathic Hospital', '9765492712', 'Homeopathic Physician', 'Private'),
(23, 'Burhani Hospital', 'Auto Lane, Amravati ?444601, Near Jamba Wadi, Amba Peth', '7212577800', 'General Physician', 'Private'),
(24, 'Burhani Hospital', 'Auto Lane, Amravati ?444601, Near Jamba Wadi, Amba Peth', '7212577800', 'Gynaecologist & Obstetrician', 'Private'),
(25, 'Burhani Hospital', 'Auto Lane, Amravati ?444601, Near Jamba Wadi, Amba Peth', '7212577800', 'Diabetologist', 'Private'),
(26, 'Burhani Hospital', 'Auto Lane, Amravati ?444601, Near Jamba Wadi, Amba Peth', '7212577800', 'Cardiologist', 'Private'),
(27, 'Burhani Hospital', 'Auto Lane, Amravati ?444601, Near Jamba Wadi, Amba Peth', '7212577800', 'General Surgeon', 'Private'),
(28, 'Sanjeevan Hospital', 'Kalyan Nagar Road, Rajapeth, Amravati ?444605', '7212677636', 'Diabetologist', 'Private'),
(29, 'Sanjeevan Hospital', 'Kalyan Nagar Road, Rajapeth, Amravati ?444605', '7212677636', 'gastroenterologists', 'Private'),
(30, 'Sanjeevan Hospital', 'Kalyan Nagar Road, Rajapeth, Amravati ?444605', '7212677636', 'General Physician', 'Private'),
(31, 'Dr. Chaudhary Physiotherapy & Ayurvedic Clinic', 'C/o Dr.Parawani Hospital, Balaji Plot, Rajapeth, Amravati ?444605, Parawani Hospital', '9960256457', 'Orthopaditian', 'Private'),
(32, 'Dr. Chaudhary Physiotherapy & Ayurvedic Clinic', 'C/o Dr.Parawani Hospital, Balaji Plot, Rajapeth, Amravati ?444605, Parawani Hospital', '9960256457', 'Physiotherapists', 'Private'),
(33, 'Dr. Chaudhary Physiotherapy & Ayurvedic Clinic', 'C/o Dr.Parawani Hospital, Balaji Plot, Rajapeth, Amravati ?444605, Parawani Hospital', '9960256457', 'Ayurvedic', 'Private'),
(34, 'Dr. Chaudhary Physiotherapy & Ayurvedic Clinic', 'C/o Dr.Parawani Hospital, Balaji Plot, Rajapeth, Amravati ?444605, Parawani Hospital', '9960256457', 'Physiotherapist For Home Visits', 'Private'),
(35, 'Dr. Chaudhary Physiotherapy & Ayurvedic Clinic', 'C/o Dr.Parawani Hospital, Balaji Plot, Rajapeth, Amravati ?444605, Parawani Hospital', '9960256457', 'Physiotherapy Centres', 'Private'),
(36, 'Dr. Chaudhary Physiotherapy & Ayurvedic Clinic', 'C/o Dr.Parawani Hospital, Balaji Plot, Rajapeth, Amravati ?444605, Parawani Hospital', '9960256457', 'Orthopaditian Physiotherapists', 'Private'),
(37, 'Dr. Chaudhary Physiotherapy & Ayurvedic Clinic', 'C/o Dr.Parawani Hospital, Balaji Plot, Rajapeth, Amravati ?444605, Parawani Hospital', '9960256457', 'Physiotherapists For Arthritis', 'Private'),
(38, 'Dr. Chaudhary Physiotherapy & Ayurvedic Clinic', 'C/o Dr.Parawani Hospital, Balaji Plot, Rajapeth, Amravati ?444605, Parawani Hospital', '9960256457', 'Physiotherapists For Foot', 'Private'),
(39, 'Dr. Chaudhary Physiotherapy & Ayurvedic Clinic', 'C/o Dr.Parawani Hospital, Balaji Plot, Rajapeth, Amravati ?444605, Parawani Hospital', '9960256457', 'Physiotherapists For Joint Pain', 'Private'),
(40, 'Parashree Speciality Hospital', 'Parashree Hospital, Bus Stand Road, Masjid to Irwin Road, Khaparde Bagicha, Amravati ?444601, Near Usmaniya Masjid', '721-2667089, 2661196,9420834219', 'General Physician', 'Private'),
(41, 'Parashree Speciality Hospital', 'Parashree Hospital, Bus Stand Road, Masjid to Irwin Road, Khaparde Bagicha, Amravati ?444601, Near Usmaniya Masjid', '721-2667089, 2661196,9420834219', 'Orthopaditian', 'Private'),
(42, 'Parashree Speciality Hospital', 'Parashree Hospital, Bus Stand Road, Masjid to Irwin Road, Khaparde Bagicha, Amravati ?444601, Near Usmaniya Masjid', '721-2667089, 2661196,9420834219', 'Pathology Labs', 'Private'),
(43, 'Parashree Speciality Hospital', 'Parashree Hospital, Bus Stand Road, Masjid to Irwin Road, Khaparde Bagicha, Amravati ?444601, Near Usmaniya Masjid', '721-2667089, 2661196,9420834219', 'Cardiologist', 'Private'),
(44, 'Parashree Speciality Hospital', 'Parashree Hospital, Bus Stand Road, Masjid to Irwin Road, Khaparde Bagicha, Amravati ?444601, Near Usmaniya Masjid', '721-2667089, 2661196,9420834219', 'Dental', 'Private'),
(45, 'Parashree Speciality Hospital', 'Parashree Hospital, Bus Stand Road, Masjid to Irwin Road, Khaparde Bagicha, Amravati ?444601, Near Usmaniya Masjid', '721-2667089, 2661196,9420834219', 'Piles', 'Private'),
(46, 'Parashree Speciality Hospital', 'Parashree Hospital, Bus Stand Road, Masjid to Irwin Road, Khaparde Bagicha, Amravati ?444601, Near Usmaniya Masjid', '721-2667089, 2661196,9420834219', 'Diabetologist', 'Private'),
(47, 'Dr. Govind Lahoti', 'Navjivan Hospital, Camp Road, Amravati 444601, Near Government Girls High School', '7212662822', 'Orthopaditian', 'Private'),
(48, 'Irwin Hospital', 'Irvin Square, Amravati', '721-2662825', 'Orthopaditian', 'Goverment'),
(49, 'Irwin Hospital', 'Irvin Square, Amravati', '721-2662825', 'General Physician', 'Goverment'),
(50, 'PDMC', 'panchawati square, Amravati', '721-2662825', 'Orthopaditian', 'Goverment'),
(51, 'PDMC', 'panchawati square, Amravati', '721-2662825', 'General Physician', 'Goverment'),
(52, 'PDMC', 'panchawati square, Amravati', '721-2662825', 'Rheumatologist', 'Goverment'),
(53, 'PDMC', 'panchawati square, Amravati', '721-2662825', 'Pulmonologist', 'Goverment'),
(54, 'PDMC', 'panchawati square, Amravati', '721-2662825', 'Diabetologist', 'Goverment');

-- --------------------------------------------------------

--
-- Table structure for table `history`
--

CREATE TABLE `history` (
  `id` int(255) NOT NULL,
  `user_id` int(200) NOT NULL,
  `sym` varchar(200) NOT NULL,
  `date` datetime(6) NOT NULL DEFAULT current_timestamp(6)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `history`
--

INSERT INTO `history` (`id`, `user_id`, `sym`, `date`) VALUES
(1, 3, 'Flu', '2024-05-01 13:22:29.269251'),
(2, 4, 'Diarrhea, Malaria, Typhoid', '2024-05-01 16:52:51.500013');

-- --------------------------------------------------------

--
-- Table structure for table `registration`
--

CREATE TABLE `registration` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `mobile` varchar(100) NOT NULL,
  `photo` varchar(100) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `registration`
--

INSERT INTO `registration` (`id`, `name`, `email`, `mobile`, `photo`, `username`, `password`) VALUES
(3, 'prashik rathi', 'prashik1@gmail.com', '1234567890', '1.jpg', 'prashik', 'prashik'),
(4, 'Vishal Rathi', 'vishal1@gmail.com', '9865322145', 'card7.png', 'vishal', '123'),
(5, 'Bhushan meshram', 'bhushan@gmail.com', '08275210641', 'demo login.jpg', 'bhushan', 'bhushan');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `doctor`
--
ALTER TABLE `doctor`
  ADD PRIMARY KEY (`did`);

--
-- Indexes for table `history`
--
ALTER TABLE `history`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `registration`
--
ALTER TABLE `registration`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `history`
--
ALTER TABLE `history`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `registration`
--
ALTER TABLE `registration`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
