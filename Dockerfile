FROM jenkins/jenkins:lts

USER root

# Installer Python
RUN apt-get update && apt-get install -y python3 python3-venv python3-pip

# Installer Git (utile parfois)
RUN apt-get install -y git

USER jenkins

