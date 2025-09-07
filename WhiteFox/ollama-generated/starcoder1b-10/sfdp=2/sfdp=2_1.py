
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(512, 512)  # Query layer
        self.key = torch.nn.Linear(512, 512)  # Key layer
        self.value = torch.nn.Linear(512, 512)  # Value layer
        self.dropout_p = dropout_p

    def forward(self, x, mask=None):
        query  = self.query(x).view(-1, 512)  # Project the input data to the query space
        key    = self.key(x).view(-1, 512)
        value  = self.value(x).view(-1, 512)

        scaled_qk  = torch.matmul(query, key.transpose(-2, -1))  # Compute the dot product of the query and the key
        inv_scale_factor  = torch.rsqrt(torch.clamp(scaled_qk + 1e-6, min=1e-6).pow(2).sum(-1)  # Compute the inverse scale factor
        softmax_qk    = scaled_qk / inv_scale_factor  # Apply softmax to the scaled dot product

        dropout_qk    = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)  # Apply dropout to the softmax output

        output        = dropout_qk.matmul(value)  # Compute the dot product of the dropout output and the value
        return output

# Initializing the model
m = Model()

