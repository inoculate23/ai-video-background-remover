from gradio_client import Client, handle_file

client = Client("http://127.0.0.1:7860/")
result = client.predict(
		video={"video":handle_file('https://github.com/gradio-app/gradio/raw/main/demo/video_component/files/world.mp4')},
		mode="Normal",
		api_name="/predict"
)
print(result)

#Accepts 2 parameters:
#video Dict(video: filepath, subtitles: filepath | None) Required

#The input value that is provided in the "video" Video component.

##mode Literal['Standard', 'Quick'] Default: "Normal"

#The input value that is provided in the "Select mode" Radio component.

#Returns 1 element
#Dict(video: filepath, subtitles: filepath | None)

#The output value that appears in the "output" Video component.