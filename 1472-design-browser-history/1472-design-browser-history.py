class BrowserHistory:

    def __init__(self, homepage: str):
        # Store all visited pages
        self.history = [homepage]

        # Index of the current page
        self.current = 0

    def visit(self, url: str) -> None:
        # Remove all pages after current page
        # because forward history is cleared
        self.history = self.history[:self.current + 1]

        # Add the new URL
        self.history.append(url)

        # Move current position to the new page
        self.current += 1

    def back(self, steps: int) -> str:
        # Move back by 'steps'
        # max(0, ...) prevents going before homepage
        self.current = max(0, self.current - steps)

        # Return current page
        return self.history[self.current]

    def forward(self, steps: int) -> str:
        # Move forward by 'steps'
        # len(self.history) - 1 is the last page
        self.current = min(
            len(self.history) - 1,
            self.current + steps
        )

        # Return current page
        return self.history[self.current]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)