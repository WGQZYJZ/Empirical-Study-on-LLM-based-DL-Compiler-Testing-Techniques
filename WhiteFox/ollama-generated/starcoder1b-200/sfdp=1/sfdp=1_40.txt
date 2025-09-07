
class Model(torch.nn.Module):
    def __init__(self, qk_ratio=0.15):
        super().__init__()
        self.qk_ratio = qk_ratio
 
    def forward(self, x1, x2):
        v1  = self._query_and_key_tensors(x1, x2) # Compute the query and key tensors
        v2 = v1 * torch.exp(-self.qk_ratio * torch.pow(torch.abs(v1), -self.params["q"] / 0.5))  # Apply a softmax function to the dot product of the two input tensors
        v3 = self._dropout_layer(v2, p=self.params["p"])  # Apply dropout to the softmax output
        return torch.matmul(torch.matmul(v1, v3), x2)  # Compute the dot product of the dropout output and the value tensor
 
    def _query_and_key_tensors(self, x1, x2):
        