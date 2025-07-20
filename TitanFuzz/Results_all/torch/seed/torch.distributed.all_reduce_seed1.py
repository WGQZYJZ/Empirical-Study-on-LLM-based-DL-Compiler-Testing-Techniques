rank = torch.distributed.get_rank()
size = torch.distributed.get_world_size()
tensor = (torch.ones(1) * rank)
torch.distributed.all_reduce(tensor, op=torch.distributed.ReduceOp.SUM)