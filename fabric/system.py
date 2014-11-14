class LocalSystem(object):
    """
    Information-gathering methods concerned with the local system.
    """
    def local_user(self):
        # FIXME: I don't understand why this was added outside the try/except,
        # but that's how the contributing user committed it. Need an older
        # Windows box to test it out, most likely.
        import getpass
        username = None
        # All Unix and most Windows systems support the getpass module.
        try:
            username = getpass.getuser()
        # Some SaaS platforms raise KeyError, implying there is no real user
        # involved. They get the default value of None.
        except KeyError:
            pass
        # Older (?) Windows systems don't support getpass well; they should
        # have the `win32` module instead.
        except ImportError:
            if win32:
                import win32api
                import win32security
                import win32profile
                username = win32api.GetUserName()
        return username