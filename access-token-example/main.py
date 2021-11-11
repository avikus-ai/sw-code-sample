
def get_access_token(self, code, state=None):
        """
        :calls: `POST /login/oauth/access_token <https://docs.github.com/en/developers/apps/identifying-and-authorizing-users-for-github-apps>`_
        :param code: string
        :param state: string
        """
        assert isinstance(code, str), code
        post_parameters = {
            "code": code,
            "client_id": self.client_id,
            "client_secret": self.client_secret,
        }

        if state is not None:
            post_parameters["state"] = state

        self._requester._Requester__authorizationHeader = None
        headers, data = self._requester.requestJsonAndCheck(
            "POST",
            "https://github.com/login/oauth/access_token",
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json",
                "User-Agent": "PyGithub/Python",
            },
            input=post_parameters,
        )

        return AccessToken(
            requester=self._requester,
            # not required, this is a NonCompletableGithubObject
            headers={},
            attributes=data,
            completed=False,
        )