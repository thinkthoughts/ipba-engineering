from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

def plot_engineering_grammar(context, output_path: Path):
    labels=context.grammar
    fig,ax=plt.subplots(figsize=(8,9.5))
    ax.axis("off")
    ys=np.linspace(0.84,0.18,len(labels))
    x=0.5
    for i,(lab,y) in enumerate(zip(labels,ys)):
        ax.add_patch(plt.Rectangle((x-.28,y-.04),.56,.08,fill=False,lw=1.8))
        ax.text(x,y,lab,ha="center",va="center",fontsize=13,
                fontweight="bold" if i<4 else "normal")
        if i<len(labels)-1:
            ax.annotate("",xy=(x,ys[i+1]+.05),xytext=(x,y-.05),
                        arrowprops=dict(arrowstyle="->",lw=1.8))
    ax.set_title("Engineering Specification Grammar")
    fig.savefig(output_path,dpi=240,bbox_inches="tight")
    return output_path

def plot_repository_lane(context, output_path: Path):
    fig,ax=plt.subplots(figsize=(12,4.8))
    ax.axis("off")
    xs=np.linspace(.12,.88,len(context.lane_symbols))
    y=.54
    for i,(x,s,l) in enumerate(zip(xs,context.lane_symbols,context.lane_labels)):
        ax.add_patch(plt.Rectangle((x-.075,y-.09),.15,.18,fill=False,lw=1.8))
        ax.text(x,y+.025,s,ha="center",fontsize=20)
        ax.text(x,y-.055,l,ha="center",fontsize=9)
        if i<len(xs)-1:
            ax.annotate("",xy=(xs[i+1]-.09,y),xytext=(x+.09,y),
                        arrowprops=dict(arrowstyle="->",lw=1.8))
    ax.set_title(context.repository_variable_title)
    ax.text(.5,.16,context.lane_caption,ha="center",fontsize=10)
    fig.savefig(output_path,dpi=240,bbox_inches="tight")
    return output_path

def plot_construction_sequence(context, output_path: Path):
    seq=context.construction_sequence
    fig,ax=plt.subplots(figsize=(max(15,len(seq)*1.35),5))
    ax.axis("off")
    xs=np.linspace(.04,.96,len(seq)); y=.53
    for i,(x,item) in enumerate(zip(xs,seq)):
        n,t=item.split(" ",1)
        ax.add_patch(plt.Rectangle((x-.041,y-.1),.082,.2,fill=False,lw=1.6))
        ax.text(x,y+.045,n,ha="center",fontweight="bold")
        ax.text(x,y-.035,t.replace(" ","\n",1),ha="center",fontsize=7.5)
        if i<len(seq)-1:
            ax.annotate("",xy=(xs[i+1]-.048,y),xytext=(x+.048,y),
                        arrowprops=dict(arrowstyle="->",lw=1.5))
    ax.set_title("Repository Construction Sequence")
    fig.savefig(output_path,dpi=240,bbox_inches="tight")
    return output_path

def generate_context_figures(context, figures_dir: Path):
    figures_dir.mkdir(parents=True,exist_ok=True)
    return {
      "grammar": plot_engineering_grammar(context, figures_dir/"00_engineering_specification_grammar.png"),
      "lane": plot_repository_lane(context, figures_dir/"00_repository_lane_specification.png"),
      "sequence": plot_construction_sequence(context, figures_dir/"00_repository_construction_sequence.png"),
    }
