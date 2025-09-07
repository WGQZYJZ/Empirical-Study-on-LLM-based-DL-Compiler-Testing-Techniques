
class Model(torch.nn.Module):
    def __init__(self, scale_factor=None, inv_scale_factor=None, dropout_p=0.5):
        super().__init__()
        
        self.scale_factor = 1 if scale_factor is None else float(scale_factor)
        self.inv_scale_factor = float(self.scale_factor**-1)
        self.dropout_p = float(dropout_p)

    def forward(self, query, key, value):
        qk = torch.matmul(query, key.transpose(-2, -1))

        scaled_qk  = qk.div(inv_scale_factor)
        
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)

        return dropout_qk.matmul(value), None


# Initializing the model
m  = Model()
scale_factor, inv_scale_factor = float(1e-6)**0.5, float(1e-7)**0.5

dropout_p  = .2

__output__, __gradOutput__  = m(torch.randn(4, 3, 8), torch.randn(4, 3, 8), \
                              torch.randn(4, 3, 8))
print(__output__.requiresGrad(), __gradOutput__.requiresGrad())

