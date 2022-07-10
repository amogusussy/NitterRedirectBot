import re
from random import randrange
import praw

reddit = praw.Reddit(client_id='')
                    client_secret='',
                    user_agent='')

subreddit = reddit.subreddit("")

instances = ["https://nitter.net/","https://nitter.42l.fr/","https://nitter.pussthecat.org/","https://nitter.fdn.fr/","https://nitter.1d4.us/","https://nitter.kavin.rocks/","https://nitter.unixfox.eu/","https://nitter.domain.glass/","https://nitter.namazso.eu/","https://birdsite.xanny.family/","https://nitter.hu/","https://nitter.moomoo.me/","https://nittereu.moomoo.me/","https://bird.trom.tf/","https://nitter.it/","https://twitter.censors.us/","https://nitter.grimneko.de/","https://n.hyperborea.cloud/","https://nitter.ca/","https://twitter.076.ne.jp/","https://nitter.fly.dev/","https://notabird.site/","https://nitter.weiler.rocks/","https://nitter.sethforprivacy.com/","https://nttr.stream/","https://nitter.cutelab.space/","https://nitter.nl/", "https://nitter.mint.lgbt/","https://nitter.bus-hit.me/","https://fuckthesacklers.network/","https://nitter.esmailelbob.xyz/","https://tw.artemislena.eu/","https://de.nttr.stream/","https://nitter.winscloud.net/","https://nitter.tiekoetter.com/","https://nitter.spaceint.fr/","https://twtr.bch.bar/","https://nitter.privacy.com.de/","https://nitter.mastodon.pro/","https://nitter.notraxx.ch/","https://nitter.poast.org/","https://nitter.bird.froth.zone/","https://nitter.dcs0.hu/","https://twitter.dr460nf1r3.org/","https://twitter.beparanoid.de/","https://n.ramle.be/","https://nitter.cz/","https://nitter.privacydev.net/","https://tweet.lambda.dance/","https://nitter.ebnar.xyz/","https://nitter.kylrth.com/","https://nitter.priv.pw/","https://nitter.foss.wtf/","https://nitter.oishi-ra.men/" ]

for submissions in subreddit.hot(limit=50):
    print("********")
    print(submission.title)

    for comment in submission.comments:
        if hasattr(comment,"body"):
            comment_lower = comment.body.lower()
            if "twitter.com" in comment_lower:
                print()
                print(comment.body)
                link = re.search("(?P<url>https?://[^\s]+)", comment_lower).group("url")
                coment.reply(f"""Twitter.com  links require you to create an account to view anything other than the main tweet body and a few replies. Use nitter instead, it allows you to view tweets without an account, and without twitter spyware.
                    Here's the same link, but with nitter instead. {link.replace("twitter.com/", instances[randrange(0, instances.len())])}
                    ***
                    This is a bot, if the instances aren't working, refer to https://github.com/xnaas/nitter-instances and contact u/Username8457.'
                    """)
