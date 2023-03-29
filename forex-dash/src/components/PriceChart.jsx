import React, { useEffect } from "react";
import Select from "./Select";
import { COUNTS } from "../app/data";
import { drawChart } from "../app/chart";

function PriceChart({
  priceData,
  selectedPair,
  selectedGranularity,
  selectedCount,
  handleCountChange,
}) {
  useEffect(() => {
    if (priceData) {
      // console.log("Draw chart ", selectedPair, selectedGranularity);
      // console.log("Draw chart ", selectedCount);
      drawChart(priceData, selectedPair, selectedGranularity, "chartDiv");
    }
  }, [priceData]);

  return (
    <div className="segment" id="price-chart-holder">
      <Select
        name="numrows"
        title="Num. Rows."
        options={COUNTS}
        defaultValue={selectedCount}
        onSelected={handleCountChange}
      />
      <div id="chartDiv"></div>
    </div>
  );
}

export default PriceChart;
