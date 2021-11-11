# 1. 아래 코드를 보고 분석해 주세요.
# 2. 코드를 보고 무슨 역할을 하는지 설명 해 보세요.
# 3. 해당 코드에서 잘 정의된 부분과 아닌 부분을 설명해 보세요.
# 4. 개선하면 좋은 부분을 찾아서 개선해 보세요.

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
