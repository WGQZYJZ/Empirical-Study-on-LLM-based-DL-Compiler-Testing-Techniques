
class Model(torch.nn.Module):
    def __init__(self, hidden_size):
        super().__init__()
        self.query = torch.nn.Linear(hidden_size, hidden_size)
        self.key   = torch.nn.Linear(hidden_size, hidden_size)

    def forward(self, x1, x2):
        v1 = self.query(x1)
        v2 = self.key(x2)
        scaled_qk = torch.matmul(v1, v2).div(math.sqrt(float(hidden_size)))  # Apply dot product
        softmax_qk = scaled_qk.softmax(dim=-1)                                  # Apply softmax on the dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)    # Apply dropout to the softmax output
        v3  = x2 * dropout_qk  # Compute dot product of dropout with value
