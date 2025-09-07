
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(512, 256)
 
    def forward(self, qk_shape):
        # Query shape: (B, H*W*C, DK) and Key shape: (B, DK, V)
        qk  = self.query(qk_shape)
        scaled_qk  = qk / scale_factor
        softmax_qk = F.softmax(scaled_qk, dim=-1)
        dropout_qk = F.dropout2d(softmax_qk, p=dropout_p)
        output      = (qk * dropout_qk).matmul(v) 
        return output

# Initializing the model
m = Model()

# Inputs to the model
qk_shape = torch.randn(batch_size, 512//8, -1)
