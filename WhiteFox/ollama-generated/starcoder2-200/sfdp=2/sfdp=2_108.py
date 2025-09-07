
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input1=None, input2=None, input3=None):  # Input with the same type and shape as the inputs to qk, scaled_qk, softmax_qk, dropout_qk, output
        v4 = torch.nn.functional.dropout(input1) # Apply dropout to the softmax output
        v5 = v4.matmul(input2)  # Compute the dot product of the dropout output and the value
        return v5


# Initializing the model
m = Model()

# Inputs to the model
qk = torch.randn(3, 8096)
key = torch.randn(3, 8096)
value = torch.randn(3, 128*7*7)
scale_factor = 0.5 # Scale factor in softmax equation for qk and scaled_qk
dropout_p = 0.5
inv_scale_factor = scale_factor.reciprocal()
__output__  = m(qk, key, value)

