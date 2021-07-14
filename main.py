import click
import ffmpeg

@click.command()
@click.option('--count', default=1, help='number of tiles')
@click.option('--delay', default=8, help='number of frames between tiles')
@click.option('--direction', default='right', help='direction of delay, "right" meaning the right-most tile is the most delayed, or "left" meaning the left-most tile is the most delayed')
@click.option('--out', help='output file name')
@click.argument('input')
def process(count, input, delay, direction, out):
    click.echo(f'Processing {input} into {count} tiles, where each tile is delayed by {delay} frames to the one on its {direction}, and saving to {out}.')
    delay_in_seconds = delay / getFrameRate(input)

    scaledSplitSrcStreams = (
        ffmpeg
        .input(input)
        .filter('scale', 640, -2)
        .filter_multi_output('split')
    )
    (
        ffmpeg
        .filter([ffmpeg.filter(scaledSplitSrcStreams[i], 'tpad', start_duration=str(delay_in_seconds * i)) for i in range(count)],
            'hstack',
            inputs=str(count))
        .output(out)
        .run()
    )

def getFrameRate(filename):
    numerator, denominator = ffmpeg.probe('circle_test.mp4')['streams'][0]['avg_frame_rate'].split('/')
    return int(numerator) / int(denominator)

if __name__ == '__main__':
    process()