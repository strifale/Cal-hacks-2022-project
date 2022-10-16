from source_files import vibeCheck
from source_files import utils

def read_sample_test():
    samples = [
            "The ones simulating us are propably getting their mind blown because we startet simulating stuff ourselfes now.",
            "when  i heard game theory i remembered fnaf", "Where\'s your Nobel peace prize",
            "Wouldn’t it be awkward if you were a hawk going back to the edge of the Circe only to find yourself sitting right next to the person you stole from?",
            "I\'m so glad I rewatched this and discovered there\'s a simulation for students to involve themselves with now. I plan on having my class use this to more thoroughly explore natural selection next year!",
            "Just done this exam, you explain everything so well!",
            "the editing at around 11:00 was insane! this is stuff i like to see",
            "Very cool video and story from your journey. I also learn Unity since a few months and its hard at the beginning, but it keeps getting better every day.",
            "just downloaded Unity and Blender hoping to make something from it for me and my friends. Didnt want to "
            "put it off too much the way i did with twitch. figured while i was thinking of it i should just do it "
            "and not wait around. Videos like this inspire me and i hope to be able to play one of your games in the "
            "future."]
    result = vibeCheck.get_inputs(samples)
    return result