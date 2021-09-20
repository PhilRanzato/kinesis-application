# kinesis-application

Python script that produces logs observed by the Amazon Kinesis Agent

## Usage

```shell
python3 kinesis-app.py
```

## Amazon Kinesis Agent

### Installation (CentOS 7)

```shell
sudo yum install –y https://s3.amazonaws.com/streaming-data-agent/aws-kinesis-agent-latest.amzn1.noarch.rpm
cp agent.json /etc/aws-kinesis/agent.json
systemctl start aws-kinesis-agent
systemctl enable aws-kinesis-agent
```

See configuration file [here](agent.json)
