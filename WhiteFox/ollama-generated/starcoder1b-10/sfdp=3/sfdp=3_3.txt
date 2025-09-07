
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query_conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.key_conv   = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1, x2):
        qk    = torch.matmul(x1, x2.transpose(-2, -1)) # Compute the dot product of the query and key tensors
        q_scaled_qk   = qk.mul(scale_factor)  # Scale the dot product by a factor
        k_softmax_qk = q_scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        v_dropout_qk = torch.nn.functional.dropout(k_softmax_qk, p=dropout_p)  # Apply dropout to the softmax output

        output  = torch.matmul(v_dropout_qk, x2) # Compute the dot product of the dropout output and the value tensor
        return output

# Initializing the model
m = Model()

