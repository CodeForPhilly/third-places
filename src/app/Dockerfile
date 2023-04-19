# Use an official Node runtime as a parent image
FROM node:16.14.0-alpine3.14

# Set the working directory to /app
WORKDIR /app

# Copy the package.json and package-lock.json to the container
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application files to the container
COPY . .

# Build the application
RUN npm run build

# Expose port 4321
EXPOSE 4321

# Start the application
CMD ["npm", "run", "host"]


