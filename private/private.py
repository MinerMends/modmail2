"""
MIT License
Copyright (c) 2020 WebKide [d.id @323578534763298816]
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import discord, traceback, random

from datetime import datetime as t
from pytz import timezone as z
from discord.ext import commands


class Private(commands.Cog):
    """─=≡Σ(つಠ益ಠ)つ private cog for my personal discord guild, it won't work for yours! """
    def __init__(self, bot):
        self.bot = bot
        self.mods = [
            ('null', 323578534763298816),
            ('DKD', 358420835108913153),
            ('VDD', 723061140816527412),
            ('alt', 324040201225633794)
        ]

    # +------------------------------------------------------------+
    # |                 PUSH-NOTIFICATION                          |
    # +------------------------------------------------------------+
    @commands.command(description='Personal Guild cmd', aliases=['poke', 'push', 'notification'], no_pm=True)  # @commands.has_any_role('Admin', 'Mod', 'DJ', 'Owner')
    async def nudge(self, ctx, *, _event_today: str = None):
        """
        ─=≡Σ(つಠ益ಠ)つ command to send a Push-notification in text-channel
        
        Usage:
        {prefix}poke [event or celebration]
        {prefix}nudge [event or celebration]
        """
        try:
            await ctx.message.delete()
        except discord.Forbidden:
            pass

        if ctx.author.id not in (mod[1] for mod in self.mods):
            return

        channel =  ctx.channel or ctx.message.channel
        e_m = f"{ctx.message.author.mention}, update this channel's **Topic** for this `command` to work!"
        h_m = "\n\n**Tip:** check other channel's Topics to get an idea of how to format their content."

        if isinstance(channel, discord.TextChannel):
            if not channel.topic:
                return await ctx.send(e_m + h_m, delete_after=23)

            if '—' in channel.topic:
                c_topic = channel.topic.replace('\n', '— ').split('—')[-1:]
                day_fix = f"{str(t.now(z('Asia/Calcutta')).strftime(f'%A %B %d'))} (IST)"
                date_fixed = day_fix.replace('1 ', '1ˢᵗ ').replace('2 ', '2ⁿᵈ ')\
                                    .replace('3 ', '3ʳᵈ ').replace('4 ', '4ᵗʰ ')\
                                    .replace('5 ', '5ᵗʰ ').replace('6 ', '6ᵗʰ ')\
                                    .replace('7 ', '7ᵗʰ ').replace('8 ', '8ᵗʰ ')\
                                    .replace('9 ', '9ᵗʰ ').replace('0 ', '0ᵗʰ ')
                if _event_today is not None:
                    h = random.choice(['for the celebration of', 'to observe', 'to honour'])
                    v = f" and to gather together {h} **{_event_today}**."
                else:
                    v = random.choice([
                        " and to continue with yesterday's topic of discussion.",
                        " where we shall pick up from yesterday's topic.",
                        " where we'll continue from where we left off yesterday.",
                        " and take part in the continuation of yesterday's discussion."
                    ])
                m = f"\U0001f538 {date_fixed} is a perfect day to listen to the "\
                    f"**{ctx.message.guild}** podcast{v}\n\n{''.join(c_topic)}"
                _nudge = await ctx.send(m)
                try:
                    await _nudge.add_reaction('thankful:695101751707303998')
                except discord.HTTPException:
                    pass

            else:
                pass
            

def setup(bot):
    bot.add_cog(Private(bot))
    
