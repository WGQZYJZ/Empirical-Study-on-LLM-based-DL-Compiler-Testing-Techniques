
class Model(torch.nn.Module):
    def __init__(self, inv_scale_factor=1):
        super().__init__()
        self.key = torch.nn.Linear(2048, 384) # 384 is an example of a hyper-parameter
        self.query = torch.nn.Linear(2048, 384)
 
    def forward(self, q, k):
        qk = torch.matmul(q, k.transpose(-2, -1)) # compute the dot product between query and key
        scaled_qk = qk / inv_scale_factor # scale by inverse scale factor
        softmax_qk = scaled_qk.softmax(-1) # apply softmax to scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.3) # apply dropout with probability 0.3
        output = qk * dropout_qk
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 2048, 64, 64)
