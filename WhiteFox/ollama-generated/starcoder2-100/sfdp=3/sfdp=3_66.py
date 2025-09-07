

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        
    def forward(self, q1: torch.Tensor = None, k1: torch.Tensor = None, v1: torch.Tensor = None) -> torch.Tensor:
        
        v2  = self.attn_layer(q1=q1, k1=k1, v1=v1)[0]
        return v2

    def attn_layer(self, q1: torch.Tensor = None, k1: torch.Tensor = None, v1: torch.Tensor = None):
        scale_factor  =  4

        scaled_qk  = self._scale_query_key(qk=torch.matmul(q1, k1.transpose(-2, -1)))
        softmax_qk  = scaled_qk.softmax(dim=-1)
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=0.387345976588916)
        output  = dropout_qk.matmul(v1)
        return (output), {}

    def _scale_query_key(self, qk: torch.Tensor):

        qk *= scale_factor
        return qk

m  = Model()

# Inputs to the model
q2  = torch.randn([50, 46])
k1  = torch.randn([50, 47, 48]).transpose(-1,-3)
v2  = torch.randn([50, 47, 49])

__output__  = m(q2=q2, k1=k1, v1=v2).numpy()

