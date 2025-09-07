
class MultiHeadedAttention(torch.nn.Module):
    def __init__(self, config):
        super().__init__()
        self._num_heads = config["n_head"]
        self._hidden_size = config["d_hidn"]
        assert (
            self._hidden_size % self._num_heads == 0
        ), "hidden_size({}) can not be divided by n_head({})".format(self._hidden_size, self._num_heads)
 
        self.key = torch.nn.Linear(config["d_hidn"], config["d_hidn"])
        self.query = torch.nn.Linear(config["d_hidn"], config["d_hidn"])
        self.value = torch.nn.Linear(config["d_hidn"], config["d_hidn"])
 
        self._scale = 1 / (self._hidden_size ** 0.5)
 
    def forward(self, query, key, value):
        v = torch.nn.functional.softmax((query @ key.transpose(-2,-1)) * self._scale + self._attn_mask)
        v = v @ value
        
        return v


# Initializing the model