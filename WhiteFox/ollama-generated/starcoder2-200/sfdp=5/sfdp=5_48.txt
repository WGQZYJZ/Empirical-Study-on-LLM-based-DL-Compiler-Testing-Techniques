
class AttentionLayer(torch.nn.Module):
    def __init__(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor, mask: torch.Tensor):
        super().__init__()

    def forward(self) -> torch.Tensor:
        qk = torch.einsum("bs...n, bs...m->bsmnm", self.__query__, self.__key__.transpose(-2, -1)) / math.sqrt(
            torch.cast(self.__query__.size(-1), "float")
            )
        attn_weight  = torch.softmax(qk + mask)
        output = attn_weight @ self.__value__
        return output


m = AttentionLayer(query, key, value, mask)
# Inputs to the model
__query__, __key__, __value__, __mask__ = torch.randn(256, 100, 48), \
                                          torch.randn(32, 100, 79, 79), \
                                          torch.randn(32, 100, 79, 79)

attn_mask = torch.randint(
    0, 
    int(-math.log(1e-5)),
    (32, ), 
     device=torch.device('cpu')
     )
attn_mask[attn_mask < -int(-math.log(1e-5))] -= attn_mask[attn_mask < -int(-math.log(1e-5))] + 10 ** -6


__output__, __attention_weight__ = m()


# What kind of PyTorch model do you want to generate? 
## please select one from [CNN, LSTM]

## If you select LSTM, please add 2 arguments as inputs. For instance, lstm(x1=torch.randn(30, 54), x2=torch.randn(79)) 
