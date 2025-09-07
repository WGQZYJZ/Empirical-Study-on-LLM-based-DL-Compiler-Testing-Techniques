
class Model(torch.nn.Module):
    def __init__(self, input_size=32, hidden_size=64):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1)
        self.pool = torch.nn.MaxPool2d(kernel_size=2, stride=2)
        self.linear1 = torch.nn.Linear(hidden_size * input_size, hidden_size)
        self.linear2 = torch.nn.Linear(hidden_size, 4)
 
    def forward(self, x):
        # Apply pointwise convolution
        v1 = self.conv1(x)
        v1 = self.pool(v1)

        # Compute query and key
        k1 = torch.bmm(v1, v1.transpose(-2, -1))  # Compute the dot product of the two input tensors (v1 @ v1.t())

        # Scale query and key
        qk = self._scale_and_apply_dropout(k1, x)

        # Apply attention mechanism with mask
        attn = self._apply_attention(qk, x)  # Compute the dot product of the dropout output and the value
        output = self.linear2(attn)  # Compute the prediction using linear function

        return output

    def _scale_and_apply_dropout(self, k1, x):
        scale = math.sqrt(k1.size(-2)) * 0.5  # Scale the query and key by sqrt(dim / N).
        k1 *= scale  # Use the scaled value to multiply the query with

        # Apply dropout
        return torch.dropout(k1, dropout_p, True)

    def _apply_attention(self, qk, x):
        attn = self._scale_and_apply_dropout(qk, x)  # Scale the attention weight
        attn = torch.softmax(attn, dim=-1)  # Use softmax to compute the confidence of the dot product

        attn *= x  # Apply the input tensor on the scaled output to obtain a new input

        return attn @ self._scale_and_apply_dropout(x, attn)  # Compute the output by using the scaled input


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
y1 = torch.randn(1, 4)
