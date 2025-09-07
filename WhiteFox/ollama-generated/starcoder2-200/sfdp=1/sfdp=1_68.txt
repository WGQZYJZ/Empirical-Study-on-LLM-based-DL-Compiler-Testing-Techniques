
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query_, key_, value_, dropout_p=0., inv_scale_factor=1.) -> torch.Tensor:
        vq  = self._apply_dotproduct(query_, key_)
        svf  = vq / inv_scale_factor
        sqk  = svf.softmax(dim=-1)
        sdqk  = torch.nn.functional.dropout(sqk, p=dropout_p)
 
        return sdqk.matmul(value_)
 
    @staticmethod
    def _apply_dotproduct(query_, key_) -> torch.Tensor:
        return query_.matmul(key_.transpose(-2, -1))


# Initializing the model
m  = Model()
 
# Inputs to the model