
class TransformerModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.key = torch.nn.Linear(768, 3072)
        self.query = torch.nn.Linear(768, 3072)
        self.value = torch.nn.Linear(768, 3072)
 
    def forward(self, query, key, value):
        # scaled_dot_product  = torch.matmul(query, key.transpose(-2, -1)) / inv_scale
        attention_weights = self._scaled_dot_product(query, key.transpose(-2, -1)).softmax(dim=-1)
        return self._attention_output(attention_weights, value)
 
    def _scaled_dot_product(self, query, key):
        