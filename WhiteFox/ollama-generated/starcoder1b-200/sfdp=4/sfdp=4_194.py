
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_layer = torch.nn.Linear(1, 2)
 
    def forward(self, x, key, value):
        ksize = key.size(-1)
        qsize = query.size(-1)

        # (B, D, K), (B, D, K)
        attn_weight = self._dot(x, query, transpose=True) / math.sqrt(key.size(-2))
        output = torch.bmm(attn_weight, value)

        return self._linear(output, keysize, qsize)

    # (B, D, K), (B, D, K), (B, D, K)
    def _dot(self, x1, x2, transpose=False):
        dim = -1 if transpose else 1
        sum_list = []
        for i in range(x1.size()[dim]):
            tmp = x1[:, :, i] * x2[:, :, i].transpose(-2, -1)
            # (B, D)
            dot = torch.bmm(tmp.contiguous().view((-1, 1)), x1[:, :, i]).view((batch_size, D))
            sum_list.append(dot)
        return torch.cat(sum_list, dim=dim).squeeze()

    # (B, K), (B, K)
    def _linear(self, x1, keysize, qsize):
        bias = self._bias

        if isinstance(bias, list):
            linear = [torch.nn.Linear(keysize, qsize, bias=bias[i], bias_attr=(False,) if bias[i] is not None else True)
                       for i in range(qsize)]
        elif bias is None:
            linear = torch.nn.Linear(keysize, qsize).weight
            torch.nn.init.orthogonal_(linear)

        return self._apply_transform(x1, linear)

    def _apply_transform(self, x1, transform):
        # (B, K), (B, K)
        return transform.contiguous().view((-1, qsize)).bmm(x1).squeeze()


# Initializing the model
m = Model()

# Inputs to the model
query  = torch.randn(1, D, K).type_as(x2)
key     = torch.randn(1, D, K).type_as(value)
value   = torch.randn(1, D, K).type_as(x2)
