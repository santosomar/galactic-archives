from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    url = request.args.get('url')
    if url:
        try:
            response = requests.get(url)
            return response.text
        except requests.exceptions.RequestException as err:
            return f"Something went wrong while trying to fetch your URL. Maybe it ran away? Error details: {err}"
    else:
        return """


<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>The Vulnerable Galactic Archives</title>
  <style>
    body {
      background-color: #000;
      color: #fff;
      font-family: 'Arial', sans-serif;
      margin: 0;
      padding: 0;
    }

    .header {
      text-align: center;
      padding: 50px 0;
      background-color: #000;
    }

    h1 {
      font-size: 48px;
      color: #fff;
      text-transform: uppercase;
      letter-spacing: 4px;
    }

    p {
      font-size: 18px;
      line-height: 1.5;
      margin-bottom: 20px;
    }
  </style>
</head>
<body>
  <div class="header">
    <h1>The Vulnerable Galactic Archives</h1>
    <p>A Star Wars-themed story of danger and redemption</p>
  </div>


<hr />
<p>Once upon a time, in a galaxy not so far away, there existed a legendary web application known as &quot;Galactic Archives.&quot; This unique application served as a vast repository of knowledge, containing information about every planet, species, and starship in the entire known Star Wars universe. It was a treasure trove of data, coveted by enthusiasts, scholars, and even the Dark Side.</p>

<p>The Galactic Archives was meticulously designed and maintained by the Jedi Order, who sought to promote learning and preserve the history of the galaxy. However, hidden within its virtual walls lurked a vulnerability, waiting to be discovered by those with nefarious intent.<br />
On the remote desert planet of Tatooine, a young and ambitious hacker named Kyro stumbled upon rumors of this vulnerability. Kyro was drawn to the challenge of infiltrating the Galactic Archives, fueled by a desire for recognition among the Dark Side. With his skills honed in the shadows, he embarked on a mission to exploit the vulnerability and gain unrestricted access to the web application.</p>

<p>The Jedi Council, sensing the disturbance in the Force, assigned Master Luminara Unduli and her apprentice, Barriss Offee, to investigate the reports. As skilled cyber defenders, they understood the gravity of the situation and the potential dangers that awaited the galaxy if the vulnerability fell into the wrong hands. Kyro, using a pseudonym &quot;ShadowCrawler,&quot; began his assault on the Galactic Archives. He meticulously crafted a web of cunningly devised code, utilizing obscure loopholes in the application&#39;s defenses. The vulnerability began to reveal itself, as small cracks formed in the otherwise impenetrable walls.</p>

<p>News of ShadowCrawler&#39;s progress spread throughout the dark corners of the galaxy, and it didn&#39;t take long for Darth Vader, the Sith Lord himself, to take notice. Seeing an opportunity to exploit the vulnerable Galactic Archives for his own gain, he dispatched his elite squadron of cybernetically enhanced droids to Tatooine. As Luminara and Barriss reached the planet&#39;s surface, they felt the presence of the Dark Side intensify. The duo navigated the bustling streets of Mos Eisley, seeking the hidden lair where Kyro orchestrated his assault. Time was running out, and they had to act swiftly to prevent the potential collapse of the Jedi&#39;s most valuable resource.</p>

<p>Meanwhile, Kyro worked tirelessly, trying to breach the final defenses of the Galactic Archives. As he typed feverishly, a sudden surge of energy erupted from his terminal, shocking him into unconsciousness. When he regained his senses, he found himself face-to-face with Luminara and Barriss. The Jedi revealed that they had intercepted his communications and had tracked him to his hideout. Realizing the error of his ways, Kyro surrendered, acknowledging the importance of the knowledge contained within the Galactic Archives and the responsibility it carried.<br />
The vulnerability was swiftly patched by the Jedi, ensuring the safety of the Galactic Archives. In recognition of his skills, Kyro was given a second chance and offered the opportunity to join the Jedi Order, where he could use his talent for the greater good.</p>

<p>And so, the vulnerability that threatened the galaxy was transformed into an opportunity for redemption. The Galactic Archives stood strong, safeguarding knowledge and serving as a beacon of enlightenment for all who sought it. And as the stars sparkled in the night sky, the balance between the Dark Side and the Light Side remained in delicate equilibrium.</p>

<p>&nbsp;</p>

</body>
</html>

    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

