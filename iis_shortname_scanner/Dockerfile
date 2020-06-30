FROM openjdk:7
RUN mkdir /iis_sns
COPY . /iis_sns
WORKDIR /iis_sns

ENTRYPOINT ["java", "-jar", "./iis_shortname_scanner.jar"]
