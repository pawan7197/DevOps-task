🔹 Step-by-Step Installation
1. 🔁 Update Package Index


sudo apt update
2. ☕ Install Java (Required for Nexus)

sudo apt install openjdk-11-jre-headless -y
You can verify the Java version with:


java -version
3. 📦 Download and Extract Nexus

wget https://download.sonatype.com/nexus/3/nexus-unix-x86-64-3.79.0-09.tar.gz
tar -xvf nexus-unix-x86-64-3.79.0-09.tar.gz
4. 📁 Move Files to /opt Directory

sudo mv nexus-3* /opt/nexus
sudo mv sonatype-work/ /opt/
5. 👤 Create a User for Nexus

sudo adduser nexus
6. 🔒 Set Ownership

sudo chown -R nexus:nexus /opt/nexus/
sudo chown -R nexus:nexus /opt/sonatype-work/
7. ⚙️ Create Nexus as a systemd Service

sudo vi /etc/systemd/system/nexus.service
Paste the following content:


[Unit]
Description=nexus service
After=network.target

[Service]
Type=forking
LimitNOFILE=65536
ExecStart=/opt/nexus/bin/nexus start
ExecStop=/opt/nexus/bin/nexus stop
User=nexus
Restart=on-abort

[Install]
WantedBy=multi-user.target
8. Enable and Start Nexus

sudo systemctl enable nexus
sudo systemctl start nexus
Check the status:


sudo systemctl status nexus
9. 🔑 Retrieve Admin Password

sudo vi /opt/sonatype-work/nexus3/admin.password
Copy the admin password shown there — you’ll need it for the web login.

🌐 Access Nexus UI
Open your browser and navigate to:


http://<public-ip-of-nexus-server>:8081
Login: admin

Password: (from admin.password file)

✅ Objective
To prepare a build server on Ubuntu to:

Install Java and Maven

Clone a Java project from GitHub

Configure Maven to connect to Nexus

Build the project

Deploy the .jar file to Nexus Repository

🔹 Prerequisites
Nexus is already installed on another EC2 server (as done previously)

Maven hosted repository (maven-releases) is created in Nexus

Admin username and password for Nexus are known

Your EC2 instance has outbound internet access to GitHub and Nexus (ensure proper security group setup)

🔹 Commands Run and Documentation
1. 📁 View files

ls
2. 🔁 Update Package List

sudo apt update
3. ✅ Check for Java (not installed yet)

java
4. ☕ Install Java (OpenJDK 11)

sudo apt install openjdk-11-jre-headless
5. 🔧 Install Maven

sudo apt install maven -y
6. 🔄 Clone the Java Project from GitHub

git clone https://github.com/pawan7197/DevOps-task.git
7. 📂 Navigate to Project Directory

cd DevOps-task/
cd java_code/
8. 🛠️ Review/Edit pom.xml to Add Nexus Deployment Info

sudo vi pom.xml
Inside <project>, add this block:


<distributionManagement>
    <repository>
        <id>nexus</id>
        <url>http://<nexus-server-public-ip>:8081/repository/maven-releases/</url>
    </repository>
</distributionManagement>
Ensure groupId, artifactId, and version are present.

9. 📦 Build the Java Project

mvn package
This creates the .jar inside target/.

10. 🔐 Configure Maven Credentials for Nexus

sudo vi /etc/maven/settings.xml
Paste the following:


<settings>
  <servers>
    <server>
      <id>nexus</id>
      <username>admin</username>
      <password>your-nexus-admin-password</password>
    </server>
  </servers>
</settings>
Make sure the <id> here matches the id in pom.xml.

11. 🚀 Deploy the Package to Nexus

mvn deploy
✅ Verification
Log into your Nexus UI:
http://<nexus-server-ip>:8081

Go to "Browse → maven-releases"

You should see your artifact under:
groupId/artifactId/version/artifact-version.jar