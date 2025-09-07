
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.matmul  = torch.matmul  # The dot product operation
        self.softmax = torch.nn.functional.softmax  # Softmax activation function

    def forward(self, query_tensor, key_tensor, value_tensor):
        qk_dot  = torch.matmul(query_tensor, key_tensor.transpose(-2, -1))  # Compute the dot product of two tensors using a predefined API

        scale_factor  = 0.75
        scaled_qk    = qk_dot * scale_factor  # Scale the output by multiplying it by another factor

        dropout_p   = 0.4
        dropout     = torch.nn.functional.dropout(scaled_qk, p=dropout_p)  # Apply dropout to the scaled dot product

        v = self.softmax(dropout) @ value_tensor  # Compute the dot product of the dropout output and a value tensor using the softmax activation function
        return v

m  = Model()

__output1__  = m(torch.randn(5, 32), torch.randn(4096, 768))
__output2__  = m(torch.randn(5, 1), torch.randn(128, 768))

