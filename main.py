import json
from datetime import datetime
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.transforms.trigger import AfterProcessingTime
from apache_beam.transforms import trigger
from apache_beam.transforms import window
from apache_beam.io.kafka import ReadFromKafka

class Output(beam.DoFn):
    def process(self, element):
        yield element

def run_stream_pipeline():
    print("--------------------- Initialising stream pipeline -----------------------------------")
    pipeline_options = PipelineOptions([
        "--runner=PortableRunner",
        "--job_endpoint=localhost:8099",
        "--environment_type=EXTERNAL",
        "--environment_config=localhost:50000",
    ])
    #print(json.dumps(pipeline_options.view_as(beam.options.pipeline_options.FlinkRunnerOptions).get_all_options(), indent=4))

    with beam.Pipeline(options=pipeline_options) as pipeline:
        (
                pipeline
                | "LoadEvents" >> beam.Create(data_simple_test)  # Load data
                | "Output variable" >> beam.ParDo(Output())         # Output
        )

        print("---------------------------------------------------------------------------------")
run_stream_pipeline()
