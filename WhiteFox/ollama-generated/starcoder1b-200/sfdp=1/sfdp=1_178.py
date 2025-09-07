
class Model(torch.nn.Module):
    def __init__(self, d_k, d_v, n_head, num_layer, pad_token=None):
        super().__init__()
        self.d_k = d_k
        self.d_v = d_v
        self.n_head = n_head
        self.num_layer = num_layer
        self.pad_token = pad_token
        self.query_conv = torch.nn.Conv2d(3, d_k * 4, 1)
        self.key_conv = torch.nn.Conv2d(3, d_k * 4, 1)
        self.value_conv = torch.nn.Conv2d(3, d_v * 4, 1)
        self.fc = torch.nn.Linear(d_k * 4 * 4, n_head * d_k * n_layer * 3)
 
    def forward(self, x):
        bsz = x.size(0)
        qkv_padding = self._get_padding(x)
        q_t1 = F.pad(self.query_conv(x), (1, 1, 1, 1), 'constant', constant_values=qkv_padding)
        q_t2 = F.pad(q_t1, (0, 1, 0, 0), 'constant', constant_values=(self.pad_token, self.pad_token))  # Apply padding token to each row of the query tensor
        q_t3 = torch.cat((q_t2[:, :, :, 0], q_t2[:, :, :, 1], q_t2[:, :, :, 2]), dim=-2)  # Concatenate row and column into a single axis
        k_t1 = F.pad(self.key_conv(x), (1, 1, 1, 1), 'constant', constant_values=qkv_padding)
        k_t2 = F.pad(k_t1, (0, 1, 0, 0), 'constant', constant_values=(self.pad_token, self.pad_token))
        k_t3 = torch.cat((k_t2[:, :, :, 0], k_t2[:, :, :, 1]), dim=-2)
        v_t1 = F.pad(self.value_conv(x), (1, 1, 1, 1), 'constant', constant_values=qkv_padding)
        v_t2 = F.pad(v_t1, (0, 1, 0, 0), 'constant', constant_values=(self.pad_token, self.pad_token))
        v_t3 = torch.cat((v_t2[:, :, :, 0], v_t2[:, :, :, 1]), dim=-2)
        qkv = torch.cat((q_t3, k_t3), dim=-1)
        # Compute the dot product of the query and key tensors
        qk = torch.matmul(qkv, k_t2.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        scaled_qk = qk.div(torch.sqrt(self.d_k).to(x.device) / math.sqrt(qkv.shape[1]))  # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = F.dropout(softmax_qk, p=self.dropout)  # Apply dropout to the softmax output
        output = F.linear(dropout_qk, v_t3.transpose(-2, -1))  # Compute the dot product of the dropout output and the value tensor
        return output
 
    def _get_padding(self, x):
        bsz = x.size(0)
        num_padding = (self.pad_token == self.pad_token).sum()
        if num_padding > 0:
            padding_idx = torch.zeros(num_padding).to(x.device)
        else:
            padding_idx = None
        return padding_idx
 
