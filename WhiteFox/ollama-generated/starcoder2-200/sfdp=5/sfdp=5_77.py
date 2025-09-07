
class AttentionModel(torch.nn.Module):
    def __init__(self, d_model=512):
        super().__init__()

        self._scale = torch.sqrt(d_model)

    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor): 
        qk  = query @ key.transpose(-2, -1) / self._scale  
        attn_mask  = torch.nn.Parameter(torch.zeros(qk.shape))
        batch_size, head_num, length_q, length_v = qk.shape

        # To mask out the padding part of each sequence (so the attention score is not zero), we first convert 0s to -inf.
        # And then set all elements outside the diagonal to inf
        np_mask  = attn_mask.detach().numpy()
        inf_mask  = -np.full(np_mask[i][j] == 0, np.NINF)

        mask1 = torch.from_numpy(np_mask).cuda()  # set to GPU first
        
        torch.nn.Parameter(mask1).masked_fill_(mask1 >= inf_mask[:, None], -inf_mask[:,None])
        torch.nn.Parameter(attn_mask)

        qk += attn_mask
        qk = torch.softmax(qk, dim=-1)
        qk = torch.dropout(qk, dropout_p=0., training=self.training_)
        output  = qk @ value
