# Extend the official Rasa SDK image
FROM rasa/rasa-sdk:latest

# Use subdirectory as working directory
WORKDIR /app

# Copy any additional custom requirements
# COPY requirements-actions.txt ./

# Change back to root user to install dependencies
USER root

# Install extra requirements for actions code, if necessary (otherwise comment this out)
# RUN pip install -r requirements-actions.txt

# Copy all files from the current directory (the actions folder) to /app
COPY . /app/actions

ENV PORT=5056

# Expose the port
EXPOSE 5056

# By best practices, don't run the code with root user
USER 1001

ENTRYPOINT [ "./entrypoint.sh" ]
CMD [ "start", "--actions", "actions", "-p 5056" ]
