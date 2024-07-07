import { cn } from "@/lib/utils"
import { IconSparkles } from "@tabler/icons-react"
import { useTheme } from "next-themes"
import { FC, SVGAttributes } from "react"

interface ModelIconProps extends SVGAttributes<SVGSVGElement> {
  height: number
  width: number
}

export const ModelIcon: FC<ModelIconProps> = ({
  height,
  width,
  ...props
}) => {
  const { theme } = useTheme()

  return (
    <IconSparkles
      height={height}
      width={width}
      className={cn(
        "rounded-sm",
        theme === "dark" ? "bg-white" : "border-DEFAULT border-black"
      )}
      {...props}
    />
  )
}