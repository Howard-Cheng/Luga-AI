import { cn } from "@/lib/utils"
import { IconSparkles } from "@tabler/icons-react"
import { useTheme } from "next-themes"
import Image from "next/image"
import { FC, HTMLAttributes } from "react"

interface ModelIconProps extends HTMLAttributes<HTMLDivElement> {
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
      size={width}
      className={cn(
        "rounded-sm",
        theme === "dark" ? "bg-white" : "border-DEFAULT border-black"
      )}
      {...props}
    />
  )
}