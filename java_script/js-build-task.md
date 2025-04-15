

### **📋 Prerequisites ** 

Before you begin, ensure you have: 

An Ubuntu Linux server (e.g., VPS or cloud instance) 

Root or sudo access 

A working internet connection 

A GitHub repository with a frontend JavaScript project (e.g., React, Vue) 

 

## **1. Switch to the Root User **

Gain administrative privileges for installing and configuring software: 

```bash 

Copy 

sudo -i
```
 

## ** 2. Install Essential Packages **

Install git to clone the project and npm to manage dependencies and build the app: 

```bash 

Copy 

apt update 
apt install git -y 
apt install npm -y
```
 
## **3. Clone the GitHub Repository ** 

Download the project from your GitHub repository: 

```bash 

Copy 

cd ~/ 
git clone https://github.com/shiva7919/Portfolio-Website.git 
cd Portfolio-Website/
```
 
## **4. Install Project Dependencies ** 

Use npm to install all required packages listed in package.json: 

```bash 

Copy 

npm install
```
 
## **5. Build the Project ** 

Build the app for production. This generates optimized static files in the build/ directory: 

```bash 

Copy 

npm run build
```
 
## **6. Install Apache Web Server **

Install Apache to serve the static files: 

```bash 

Copy 

apt install apache2 -y
```
 
 ## **7. Deploy the Build to Apache’s Web Root **

Clear the default Apache content and copy your built files: 

```bash 

Copy 

cd /var/www/html/ 
rm -rf * 
cp -r ~/Portfolio-Website/build/* .
```
 

## **8. Restart Apache to Apply Changes **

Reload the Apache server to serve your newly deployed app: 

```bash 

Copy 

systemctl restart apache2
```
 
## **✅ Conclusion **

Your JavaScript application is now successfully built and deployed on your Ubuntu server. It is being served via Apache as a static site. 

You can access your application by entering your server's IP address or domain name in a web browser: 

This setup is ideal for deploying single-page applications (SPAs) like those built with React, Vue, or Angular, using Apache as a simple static file server..

 

## ** 9.Final Output: **

![](./img/Screenshot%20(2).png)
