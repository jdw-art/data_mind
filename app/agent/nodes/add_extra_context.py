"""
额外上下文补充节点

负责在生成 SQL 前整理完整提示词上下文
例如候选表结构 字段说明 指标口径 取值映射以及必要的业务规则
"""

from langgraph.runtime import Runtime

from app.agent.context import DataAgentContext
from app.agent.state import DataAgentState
from app.core.log import logger

async def add_extra_context(state: DataAgentState, runtime: Runtime[DataAgentState]):
    """补齐生成 SQL 所需的上下文信息"""

    writer = runtime.stream_writer
    # 这里是过滤结果汇合点，后续会把结构化上下文写回到 state
    writer("添加额外上下文")
    import asyncio

    # 当前章节先用 sleep 模拟真实节点耗时，后续会替换为 LLM 或规则抽取逻辑
    await asyncio.sleep(0.5)