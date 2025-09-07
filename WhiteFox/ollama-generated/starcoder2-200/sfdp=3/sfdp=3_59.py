
class SelfAttentionModel(torch.nn.Module):
    def __init__(self, query: torch.Tensor, key: torch.Tensor) -> None:
        super().__init__()
        self._scale = 64
        self._dropout_p = 0.1

        self.query = query
        self.key   = key

    @staticmethod
    def _softmax(scaled):
        