import rumps


class MeineApp(rumps.App):

    @rumps.clicked("Begrüßen")
    def sayhi(self, _):
        rumps.alert('Moin moin!')


MeineApp("Meine App").run()
